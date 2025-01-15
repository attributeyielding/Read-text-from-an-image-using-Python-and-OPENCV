<!-- Doc 2 is in language en-US. Optimizing Doc 2 for scanning, using lists and bold where appropriate, but keeping language en-US, and adding id attributes to every HTML element: --><h3 id="u6wl39f">Key Features</h3>
<ol id="9pg8jtn">
<li id="w4lf25q">
<p id="zgt6o9o"><strong>Preprocessing Options</strong>:</p>
<ul id="pxmjj9">
<li id="cgpfh5b"><strong>Thresholding</strong>: Converts the image into a binary image, enhancing <strong>text visibility</strong> against the background.</li>
<li id="yu7l1o"><strong>Blurring</strong>: Reduces <strong>noise</strong> and smoothens the image.</li>
<li id="nu8op2d"><strong>Edge Detection</strong>: Highlights <strong>text contours</strong>, useful for sharp text or images with strong contrasts.</li>
</ul>
</li>
<li id="e11lat">
<p id="1j2maoc"><strong>Dynamic Preprocessing</strong>:</p>
<ul id="8m0mpr">
<li id="pk46ubz">The <code id="4pfhceb">preprocess_method</code> parameter allows switching between methods for <strong>experimentation</strong>.</li>
</ul>
</li>
<li id="0r7a3fy">
<p id="yru1n77"><strong>Scalable Design</strong>:</p>
<ul id="wce3np7">
<li id="vb1yyt">Easily <strong>extendable</strong> for more preprocessing techniques if needed.</li>
</ul>
</li>
</ol>
<h3 id="csdtaio">How to Use</h3>
<ol id="10muwz">
<li id="aholkuc">Save the script to a file, e.g., <code id="9i702es">ocr_reader.py</code>.</li>
<li id="n02ytjl">Update the <code id="41nw0cp">tesseract_executable_path</code> variable if required.</li>
<li id="o14vbvi">Replace <code id="7vugayb">example_image.jpg</code> with your <strong>image path</strong>.</li>
<li id="hnx47i8">Run the script to see OCR results using different preprocessing methods:
<pre id="ts1ldyi">
<code id="wu4nvf2tc">python ocr_reader.py
</code>
</pre>
</li>
</ol>
<p id="1ndaneg">Let me know if you need further <strong>customization</strong> or <strong>explanation</strong> of any part of the code!</p>
