# Import required libraries
import cv2  # OpenCV for image processing
import pytesseract  # Tesseract OCR library for text extraction

class OCRReader:
    """
    A class for extracting text from images using OpenCV and Tesseract OCR.
    """

    def __init__(self, tesseract_path=None):
        """
        Initialize the OCRReader class.

        Args:
            tesseract_path (str): Path to the Tesseract executable (required on Windows).
        """
        if tesseract_path:
            # Set the Tesseract executable path (only required for Windows users)
            pytesseract.pytesseract.tesseract_cmd = tesseract_path

    @staticmethod
    def preprocess_image(image_path, method="threshold"):
        """
        Load and preprocess the image for better OCR performance.

        Args:
            image_path (str): Path to the image file.
            method (str): Preprocessing method to use. Options:
                          - "threshold": Apply thresholding (default).
                          - "blur": Apply Gaussian blur.
                          - "edge": Apply edge detection.

        Returns:
            ndarray: Preprocessed image.
        """
        # Read the image from the file
        image = cv2.imread(image_path)

        # Convert the image to grayscale to reduce complexity
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply the selected preprocessing method
        if method == "threshold":
            # Apply thresholding to enhance text visibility
            _, processed_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        elif method == "blur":
            # Apply Gaussian blur to reduce noise
            processed_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        elif method == "edge":
            # Apply edge detection using Canny
            processed_image = cv2.Canny(gray_image, 100, 200)
        else:
            # Default to the grayscale image if an invalid method is provided
            processed_image = gray_image

        return processed_image

    def extract_text(self, image_path, lang="eng", config="", preprocess_method="threshold"):
        """
        Extract text from the provided image.

        Args:
            image_path (str): Path to the image file.
            lang (str): Language for OCR (default is English).
            config (str): Custom Tesseract configuration options.
            preprocess_method (str): Preprocessing method to use. Options:
                                     - "threshold"
                                     - "blur"
                                     - "edge"

        Returns:
            str: Extracted text from the image.
        """
        # Preprocess the image
        processed_image = self.preprocess_image(image_path, method=preprocess_method)

        # Use Tesseract to extract text from the image
        extracted_text = pytesseract.image_to_string(processed_image, lang=lang, config=config)

        return extracted_text


# Example usage of the OCRReader library
if __name__ == "__main__":
    # Specify the path to the Tesseract executable (required for Windows users)
    # Example: r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    tesseract_executable_path = None  # Update if using Windows

    # Initialize the OCRReader
    ocr_reader = OCRReader(tesseract_path=tesseract_executable_path)

    # Path to the image file
    image_file = "example_image.jpg"

    # Extract text from the image using different preprocessing methods
    for method in ["threshold", "blur", "edge"]:
        print(f"\nExtracting text using preprocessing method: {method}")
        extracted_text = ocr_reader.extract_text(image_file, preprocess_method=method)
        print("Extracted Text:")
        print(extracted_text)
