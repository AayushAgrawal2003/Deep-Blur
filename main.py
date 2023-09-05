import cv2
import numpy as np

image_path = 'test.jpg'  
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

def add_blur(image):
    kernel_size = (5, 5)  # You can change these values
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    return blurred_image

def sharpen_image(image):
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])

    # Apply the sharpening filter to the image
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image

def calculate_var(image):
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    laplacian_variance = np.var(laplacian)
    return laplacian_variance

def split_image(image):
    height, width  = image.shape
    # Calculate the midpoint to split the image vertically
    midpoint = width // 2

    # Split the image into two parts
    left_part = image[:, :midpoint]
    right_part = image[:, midpoint:]

    return left_part, right_part


def concat(image1, image2):
    concatenated_image = np.hstack((image1, image2))

    return concatenated_image





# Display the original image and Laplacian image (optional)

left, right = split_image(image)

mixed = concat(add_blur(left), sharpen_image(right))

print("Laplacian Variance Before Blurring:", calculate_var(image))
print("Laplacian Variance After mixing:", calculate_var(mixed))
# print("Laplacian Variance After Sharpening:", calculate_var(sharpen_image(image)))

# cv2.imshow('Original Image',left )
# cv2.imshow('Laplacian Image', right)
cv2.imshow('Laplacian Image', mixed)
cv2.waitKey(0)
cv2.destroyAllWindows()
