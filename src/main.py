from utils import load_data, evaluate_bias

def main():
    data = load_data("data/sample_data.csv")
    result = evaluate_bias(data)
    print(result)

if __name__ == "__main__":
    main()
