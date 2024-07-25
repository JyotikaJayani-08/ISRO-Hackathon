# ISRO-Hackathon
Team Cosmo Coders

![image](https://github.com/user-attachments/assets/9c5b5540-1a33-4827-808a-0dc94b9dcc7c)

Topic-Image based Search of Lunar craters from global mosaic

Main Components of the Project-

1.A fine-tuned YOLOv4 model for lunar crater detection

2.An API built using Roboflow for model deployment and inference

3.A web application developed with Flask, HTML, and inline CSS for user interaction

<img width="960" alt="image" src="https://github.com/user-attachments/assets/33afdd10-1183-48a7-9f53-618ba3016742">
<img width="960" alt="image" src="https://github.com/user-attachments/assets/70bbe488-0f35-4f90-bd06-3d030d9c08a6">

  Steps and Key Insights-
  1.Dataset Preparation

  2.Data Augmentation

  3.Model Architecture(Yolov Model)

  4.Training Process

  5.Training statistics:
  Total training time: 72 hours
  Final mAP (mean Average Precision) @ IoU 0.5: 0.92
  Final mAP @ IoU 0.5:0.95: 0.78
  Inference speed: 30 FPS on a single NVIDIA RTX 3080 GPU

 6.Post-processing

 7.API Development using Roboflow

 8.Model Export

 9.Model Deployment
 Roboflow automatically generated an API endpoint for our model. The endpoint URL follows this format-
 https://detect.roboflow.com/lunar-crater-detection/1

 10.Web Application Development with Flask



