import csv
import os
import shutil

from PIL import Image, ImageDraw, ImageFont
from slugify import slugify


class Certificate:
    def __init__(self, template_name, attendee_name, project_name):
        self.template_name = template_name
        self.attendee_name = attendee_name
        self.project_name = project_name

    def generate_certificate(
        self,
        font_style="Roboto-Thin.ttf",
        name_size=100,
        project_size=70,
        name_height=600,
        project_height=900,
        file_name="result.png",
        name_color=(35, 57, 75),
        project_color=(35, 57, 75),
        name_offset=0,
        project_offset=80,
    ):

        empty_img = Image.open(self.template_name)
        img_w, _ = empty_img.size

        # name
        name = self.attendee_name
        n_height = name_height
        font = ImageFont.truetype(font_style, name_size)
        font_w, _ = font.getsize(name)
        name_h_centre = img_w / 2 - font_w / 2 + name_offset

        # project
        project = self.project_name
        project_font_size = project_size
        p_height = project_height
        project_font = ImageFont.truetype(font_style, project_font_size)
        p_font_w, _ = font.getsize(project)
        project_h_centre = img_w / 2 - p_font_w / 2 + project_offset

        # name
        image_editable = ImageDraw.Draw(empty_img)
        image_editable.text((name_h_centre, n_height), name, name_color, font=font)
        empty_img.save(file_name)

        # project
        image_w_name = Image.open(file_name)
        image_editable_p = ImageDraw.Draw(image_w_name)
        image_editable_p.text(
            (project_h_centre, p_height), project, project_color, font=project_font
        )
        image_w_name.save(file_name)


def serve_images(name_project_list, include_csv=True):

    # create image folder
    img_folder = "./participants/"
    try:
        os.mkdir(img_folder)
    except OSError:
        pass

    for name, project, _ in name_project_list:
        file_name = slugify(name) + ".png"

        cert = Certificate(
            "/app/staticfiles/images/certificate/empty_cert.png", name, project
        )
        cert.generate_certificate(
            "/app/staticfiles/fonts/Roboto-Thin.ttf", file_name=img_folder + file_name
        )

    # add csv
    if include_csv:
        fields = ["Name", "Project", "Email"]

        with open(img_folder + "all_participants.csv", "w") as f:
            write = csv.writer(f)
            write.writerow(fields)
            write.writerows(name_project_list)

    # make zip folder
    shutil.make_archive("participants", "zip", img_folder)

    # delete folder after creating zip
    shutil.rmtree(img_folder)


def get_event_participants(event):
    """
    Returns a list of name and projects to an event
    """

    name_project_list = []

    for participant in event.participants.all():
        name = participant.name

        # dont add empty name
        if name != "":
            name_project_list.append([participant.name, event.title, participant.email])

    return name_project_list
