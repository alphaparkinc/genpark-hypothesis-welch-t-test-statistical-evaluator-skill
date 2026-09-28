from client import HypothesisWelchTTestEvaluator
import json

def main():
    evaluator = HypothesisWelchTTestEvaluator()
    res = evaluator.run_benchmark_welch_t_test()
    print("Welch's T-Test Benchmark Result:")
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
