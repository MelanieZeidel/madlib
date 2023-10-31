from madlibs_samples import fairytail,sports
import random 

if __name__ == "__main__":
    m = random.choice([fairytail,sports])
    m.completed_text()