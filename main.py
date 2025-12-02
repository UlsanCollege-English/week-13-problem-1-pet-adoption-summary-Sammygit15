def summarize_adoptions(adoptions):
  
    counts = {}  # dictionary to store animal -> count

    for animal in adoptions:
        if animal in counts:
            counts[animal] += 1
        else:
            counts[animal] = 1

    return counts


if __name__ == "__main__":
    # Optional manual test
    sample = ["cat", "dog", "cat", "rabbit", "dog", "cat"]
    print(summarize_adoptions(sample))
