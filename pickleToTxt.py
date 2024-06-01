import pickle

pickle_file_path = 'tmp/rollouts/waterdrop_waterramps/train1_2162818/radius_0.015/rollout_test_0.pkl'

output_txt_file_path = 'tmp/rollouts/waterdrop_waterramps/train1_2162818/output.txt'


with open(pickle_file_path, 'rb') as file:
    data = pickle.load(file)


with open(output_txt_file_path, 'w') as txt_file:
    txt_file.write(str(data))
