# Deep Blur 

We analyzed the results of the laplacian filter and put it in situations where a particular portion of the image was blurred and the results showed that the value of the lapacian is significantly higher than it should be. This is where classical methods fail.

Our Solution:

We propose a RPN based approach were we predict the regions of blur and then based on this calculate the value of the blur. Essentially we are running a semantic segmentation model to calculate the region where the blur is high. 

Then we can run the laplacian model on this region to calculate the appropriate value. We will need to calculate a metric that can make use of the size of the semantic segmentation model output and the laplacian value of the region. 

## Models tested 

1. U-NET
2. Masked RCNN 

## Dataset 

1. We generate images using a random blur initiator. We will add Gaussian noise to random locations in the image and then we will use this as an input to the segmentation model. 




