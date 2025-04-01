View
====

The View tab provides powerful visualization and exploration capabilities for protein expression data and multi-channel microscopy images. This interface allows researchers to visualize, layer, and manipulate multiple data channels to gain insights into protein distribution at the single-cell level.

.. note::
   To include the view tab image in this documentation, save a screenshot of the view tab to the docs/source/_static directory with the filename "view_tab.png".

.. image:: _static/view_tab.png
   :width: 600
   :alt: View tab interface

Interface Overview
-----------------

The View tab consists of two main sections:

1. **Layer Control Panel** (left): Manage individual protein/image layers and their display properties
2. **Visualization Canvas** (right): Display the combined image with interactive region selection tools

Layer Management
---------------

Add Layer
^^^^^^^^

The "Add Layer" button allows you to select and add protein channels from your dataset to the visualization. Each protein channel is displayed as a separate layer that can be independently manipulated.

Add Other Image
^^^^^^^^^^^^^^

Use this button to import additional images (PNG, JPG, TIFF, etc.) as overlays. This is useful for adding reference images or annotations to your visualization.

Layer Controls
-------------

Each layer added to the visualization has its own control panel with the following options:

Opacity
^^^^^^^

A slider control (0-100%) that adjusts the transparency of the layer. This allows for better visualization of overlapping features.

Contrast
^^^^^^^^

A dual-slider control that adjusts the minimum and maximum intensity values displayed. This enables you to highlight specific intensity ranges within your data:

* Left slider: Sets the minimum intensity threshold (values below this will appear black)
* Right slider: Sets the maximum intensity threshold (values above this will be displayed at maximum brightness)

Adjusting these values helps to reveal structures that might be hidden in the original intensity range.

Visibility
^^^^^^^^^

The "Toggle Visibility" button lets you show or hide specific layers without removing them from your layer stack. This is useful for comparing different protein expression patterns.

Tint Color
^^^^^^^^^

The "Select Tint Color" button opens a color selection dialog that allows you to apply a color tint to your grayscale protein data. Common colors include:

* Red, Green, Blue (primary colors for multi-channel visualization)
* Cyan, Magenta, Yellow (complementary colors)
* Custom colors for specific protein highlighting

Delete Layer
^^^^^^^^^^^

Removes the selected layer from the visualization.

Visualization Canvas
-------------------

The main canvas displays the combined image with all visible layers according to their opacity, contrast, and tint settings.

Region Selection Tools
^^^^^^^^^^^^^^^^^^^^^

In the top right corner of the canvas, you'll find tools for selecting regions of interest:

* **Rectangle Selection**: Select rectangular regions for detailed analysis
* **Circle/Ellipse Selection**: Select circular regions of interest
* **Custom Region Selection**: Draw custom shapes to isolate specific structures

These selection tools help you focus your analysis on specific areas of the image.

Data Loading and Processing
--------------------------

Before visualization, you need to load your data:

1. **Open Image**: Load the cell segmentation image (typically a StarDist output)
2. **Open Cell Data**: Load the corresponding protein expression data (CSV or Excel format)
3. **Scale Down Factor**: Adjust the image resolution for performance optimization
4. **Apply**: Process and prepare the data for visualization

For large datasets, the application uses efficient parallel processing to handle the visualization rendering.

Technical Details
----------------

The View tab implements several advanced techniques for efficient protein visualization:

1. **JIT Compilation**: Just-in-time compilation is used for the protein visualization algorithm to maximize performance.

2. **Efficient Contrast Adjustment**: Uses percentile-based windowing to enhance visual contrast without altering the underlying data.

3. **Color Mapping**: Applies scientific color maps to grayscale data for better differentiation of structures.

4. **Layer Compositing**: Uses alpha compositing for smooth blending of multiple protein channels.

Usage Tips
---------

* **Multi-channel Visualization**: Assign different colors to different protein channels to create informative multi-channel overlays
* **Contrast Adjustment**: For faint signals, narrow the contrast range to make them more visible
* **Strategic Coloring**: Use complementary colors for proteins that co-localize to better visualize their spatial relationships
* **Region Selection**: Use selection tools to focus on areas of interest for more detailed quantitative analysis
* **Layer Organization**: Order your layers strategically with the most important data on top for optimal visualization
