import sys, json
from client import HypothesisWelchTTestEvaluator

def main():
    evaluator = HypothesisWelchTTestEvaluator()
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        try:
            req = json.loads(line)
            method = req.get("method")
            rid = req.get("id")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "tools": [
                        {"name": "evaluate_welch_t_test", "description": "Run Welch t-test.", "inputSchema": {"type": "object", "properties": {"group_a": {"type": "array"}, "group_b": {"type": "array"}}, "required": ["group_a", "group_b"]}},
                        {"name": "run_benchmark_welch_t_test", "description": "Run self-test.", "inputSchema": {"type": "object"}}
                    ]
                }
            elif method == "tools/call":
                tname = params.get("name")
                args = params.get("arguments", {})
                if tname == "evaluate_welch_t_test":
                    out = evaluator.evaluate_welch_t_test(args.get("group_a", []), args.get("group_b", []))
                elif tname == "run_benchmark_welch_t_test":
                    out = evaluator.run_benchmark_welch_t_test()
                else:
                    out = {"error": f"Unknown tool {tname}"}
                res = {"content": [{"type": "text", "text": json.dumps(out)}]}
            else:
                res = {"error": "Unsupported method"}
            print(json.dumps({"jsonrpc": "2.0", "id": rid, "result": res}), flush=True)
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}), flush=True)

if __name__ == "__main__":
    main()
