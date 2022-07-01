from TALLDataset import TestingDataSet
train_csv_path = "./exp_data/TACoS/train_clip-sentvec.pkl"
test_csv_path = "./exp_data/TACoS/test_clip-sentvec.pkl"
train_feature_dir = "G:/TALL by author/TACOS/Interval64_128_256_512_overlap0.8_c3d_fc6/"
test_feature_dir = "G:/TALL by author/TACOS/Interval128_256_overlap0.8_c3d_fc6/"
frames_info_path = "video_allframes_info.pkl"
batch_size = 56
epochs = 2
test_data = TestingDataSet(test_feature_dir, test_csv_path, 1)
print(len(test_data.movie_names))
for movie_name in test_data.movie_names:
    s = test_data.load_movie_slidingclip(movie_name)
    print(s[0])
    print(s[1])