This python program uses YOLOv8 to detect objects.
First we download the YOLOv8s model and then train it on our custom datset
The data is given in the required format in Data folder.
Model_training.py is used to train the model while Model_testing.py is used to test the model.

The model as well as perfomance metrics are given in the runs/detect/<trainx> (<trainx> is to be replaced with train followed by a number)

The model was trained in several stages.
During the first 4 stages the model was becoming more and more accurate, but from the 5th training onwards, the accuracy on the validation dataset started decreasing due to overfitting of the model.
(The ones initally trained after train4 were deleted and replaced by newer models)
Then, I tried to mitigate overfitting by trying various strategies such as changing parameters like warmup_epochs, close_mosaics, optimizer, learning rates and weights of classification and box losses.
I tried other strategies such as removing a certain percentage of random images from the dataset in an epoch and cosine annealing of learning rate and training the model in batches of 5, taking the best model out of each batch for the next training.
I also tried training it over another new dataset and alternating between the 2 datasets.
But nothing worked very well.
Increasing the weightage of the box loss in the overall loss function (untill Train9) resulted in the model detecting slightly more number of objects at the cost of slightly higher false positive rate.
Increasing the weight again (until Train12) resulted in even higher number of objects detected at the cost of significantly higher false positive rate.
Then, hoping to keep the higher detection rate while lowering the false positive rate, I tried increasing the weightage of classification loss and decreasing the weightage of box loss , I obtained a slightly lower number of objects detected with a lower false positive rate.

The Train4 model is the best so far, having a low false positive rate with a decent detection rate.
In order to make the model better, more data is needed.
(This folder contains only train4 weights to stay under 100 mb)

Requirements:

Ultralytics library : pip install ultralytics