def load_data():
    import pandas as pd
    hn_stories=pd.read_csv('hn_stories.csv',names=["submission_time","upvotes","url","headline"])
    return hn_stories

    
if __name__=="__main__":
    import pandas as pd
    import numpy as np
    load_data()