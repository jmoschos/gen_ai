from ml_pipeline import Pipeline
from hugging_face import Solution

if __name__ == '__main__':
    #Pipeline().run()
    solution = Solution.with_default_model()
    result = solution.get_sentiment("I think it was the best thing ive ever seen.")
    print(result)