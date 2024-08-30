def find_runner_up_score():
    n = int(input("Enter the number of scores: "))
    scores = list(map(int, input("Enter the scores separated by space: ").split()))
    
    # Convert scores to a set to remove duplicates
    unique_scores = set(scores)
    
    # Remove the maximum score
    unique_scores.remove(max(unique_scores))
    
    # The runner-up score is the maximum of the remaining scores
    runner_up_score = max(unique_scores)
    
    print("The runner-up score is:", runner_up_score)

# Call the function to test
find_runner_up_score()
