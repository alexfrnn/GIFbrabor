import os
import uuid
import io
import base64
from flask import Flask, request, render_template
import imageio.v3 as iio

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    gif_url = None
    gif_filename = None
    if request.method == "POST":
        files = request.files.getlist("images")
        images = []
        for file in files:
            image = iio.imread(file.stream)
            images.append(image)

        output_gif = io.BytesIO()
        iio.imwrite(output_gif, images, format="GIF", duration=500, loop=0)
        output_gif.seek(0)

        gif_data = base64.b64encode(output_gif.getvalue()).decode('utf-8')
        gif_url = f"data:image/gif;base64,{gif_data}"
        gif_filename = f"{uuid.uuid4()}.gif"

    return render_template("index.html", gif_url=gif_url, gif_filename=gif_filename)

if __name__ == "__main__":
    app.run(debug=True)