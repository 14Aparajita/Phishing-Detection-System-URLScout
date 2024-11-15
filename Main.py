

from API import get_prediction

# path to trained model
model_path = r"C:\MyFolders\Projects\minor project\patent2\Malicious_URL_Prediction.h5"

# input url
url = "https://chatgpt.com/"

# returns probability of url being malicious
prediction = get_prediction(url,model_path)
print(prediction)

