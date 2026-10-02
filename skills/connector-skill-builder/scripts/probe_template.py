# -*- coding: utf-8 -*-
"""通用 TCP socket 探针模板：心跳 / 读状态 / 执行 / 回传。

按目标软件的协议修改 HOST / PORT 与消息构造、解析部分；
CLI / HTTP / SDK 通道参考本模板的"四步验证"顺序改写。
"""
import socket, json, time

HOST = "127.0.0.1"
PORT = 9876                   # 改为目标软件端口
TYPE_PING = "ping"            # 心跳消息类型
TYPE_STATE = "get_scene_info" # 读状态消息类型
TYPE_EXEC = "execute_code"    # 执行消息类型


def send(cmd, timeout=10):
    """发送一条 JSON 消息并等待完整 JSON 响应。"""
    s = socket.create_connection((HOST, PORT), timeout=timeout)
    s.sendall(json.dumps(cmd).encode("utf-8") + b"\n")
    buf = b""
    end = time.time() + timeout
    while time.time() < end:
        try:
            chunk = s.recv(8192)
            if not chunk:
                break
            buf += chunk
            try:
                r = json.loads(buf.decode("utf-8"))
                s.close()
                return r
            except Exception:
                pass
        except socket.timeout:
            break
    s.close()
    return {"status": "timeout", "raw": buf[:300].decode("utf-8", errors="replace")}


if __name__ == "__main__":
    print("1 心跳:", json.dumps(send({"type": TYPE_PING}), ensure_ascii=False)[:200])
    print("2 状态:", json.dumps(send({"type": TYPE_STATE}), ensure_ascii=False)[:400])
    print("3 执行:", json.dumps(
        send({"type": TYPE_EXEC, "params": {"code": "print('PROBE_OK')"}}),
        ensure_ascii=False)[:300])
    # 4 回传：截图 / 文件输出，按目标协议扩展后落盘
