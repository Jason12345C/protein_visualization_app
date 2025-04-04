Preprocessing
=============

The Preprocessing tab provides essential image preparation functionality needed before analysis of scientific images, particularly for protein visualization. This tab contains several key tools for manipulating and optimizing images.

.. note::
   To include the preprocessing tab image in this documentation, save a screenshot of the preprocessing tab to the docs/source/_static directory with the filename "preprocessing_tab.png".

.. image:: _static/preprocessing_tab.png
   :width: 600
   :alt: Preprocessing tab interface

Basic Image Manipulation
-----------------------

Crop
^^^^

The cropping tool allows you to select a region of interest within your image. Two options are available:

* **Image Selection Tool**: Click the image icon to manually select a portion of your image to crop.
* **Clear Selection**: Click the X icon to clear your current selection and start over.

Rotate
^^^^^^

The rotation tool provides a slider to adjust the orientation of your image. After setting the desired rotation angle:

* Click **Ok** to apply the rotation.

Image Alignment
--------------

The Align Layers section provides tools to align multiple microscopy channels or images.

Align with Blue Color
^^^^^^^^^^^^^^^^^^^^

A dropdown selection (Yes/No) to determine whether the blue fluorescence channel should be used as a reference for alignment. This is commonly used when DAPI or Hoechst staining is present in your samples.

Alignment Layer
^^^^^^^^^^^^^^

A dropdown menu to select which channel should be used as the reference layer for alignment. The registration algorithm will align all other channels to this reference.

Cell Layer
^^^^^^^^^

Select which channel contains your cell morphology information. This is typically a channel that shows cell membranes, nuclei, or other cellular structures clearly.

Protein Detection Layer
^^^^^^^^^^^^^^^^^^^^^^

Select the channel containing the protein of interest that you wish to analyze. This is typically where your target protein fluorescence is detected.

Alignment Settings
^^^^^^^^^^^^^^^^^

* **Max Size**: Sets the maximum dimension (in pixels) for processing during alignment (default: 23000). Larger images will be downsampled to this size.
* **Number of Tiles**: Determines how many tiles the image will be divided into for alignment (default: 5). More tiles can improve alignment accuracy for complex images but increases processing time.
* **Overlap**: Specifies the pixel overlap between adjacent tiles (default: 500). Proper overlap ensures seamless alignment between tiles.

Once settings are configured, click **Run** to perform the alignment, or **Cancel** to abort the operation.

Smoothing
---------

The smoothing slider (0-100%) applies a smoothing algorithm to reduce noise in your images. The intensity of smoothing can be adjusted using the slider, with 0% representing no smoothing and 100% representing maximum smoothing.

After adjusting the smoothing level, click **Replace with smoothed layer** to apply the changes.

Cell Segmentation
----------------

The StarDist Cell Segmentation section provides tools for automated cell detection using deep learning.

Select Channel
^^^^^^^^^^^^^

Choose which image channel to use for cell detection. Typically this should be a channel that clearly shows cell boundaries or nuclei.

Pre-trained 2D Model
^^^^^^^^^^^^^^^^^^^

Select from available pre-trained StarDist models for cell segmentation. The default model (2D_versatile_fluo) works well for most fluorescence microscopy images.

Segmentation Parameters
^^^^^^^^^^^^^^^^^^^^^^

* **Percentile Low**: Sets the lower percentile threshold for image normalization (default: 3.00).
* **Percentile High**: Sets the upper percentile threshold for image normalization (default: 99.80).
* **Probability/Score Threshold**: Defines the confidence threshold for cell detection (default: 0.48). Higher values result in more conservative detection.
* **Overlap Threshold**: Determines how much overlap is allowed between adjacent cells (default: 0.30). Lower values allow more overlap.

Technical Details
----------------

The Preprocessing tab leverages several advanced algorithms:

1. **Image Registration**: Utilizes feature-based alignment techniques to precisely align different image channels or sequential images. The alignment process uses a tiled approach to handle large microscopy images efficiently.

2. **StarDist Segmentation**: Implements the StarDist deep learning model for accurate cell segmentation in fluorescence microscopy images. This model uses star-convex polygons to represent cell shapes and boundaries.

3. **Parallel Processing**: Operations utilize GPU acceleration when available for faster processing of large datasets.

Usage Tips
---------

* For optimal results, ensure that the alignment channel has clear, distinct features.
* When working with large datasets, consider reducing the Max Size parameter to speed up processing.
* Adjust segmentation parameters based on your specific cell type and image quality.
* For noisy images, apply smoothing before segmentation to improve detection accuracy.
