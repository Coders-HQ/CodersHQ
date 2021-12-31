from PIL import Image, ImageFont, ImageDraw 
import pandas as pd

class Certificate:
  

  def __init__(self, template_name, attendee_name, project_name):
    self.template_name = template_name
    self.attendee_name = attendee_name
    self.project_name = project_name

  def generate_certificate(self, 
                           font_style="Roboto-Thin.ttf",
                           name_size=100,
                           project_size=70,
                           name_height=600,
                           project_height=900,
                           file_name="result.png",
                           name_color=(35, 57, 75),
                           project_color=(35, 57, 75),
                           name_offset=0,
                           project_offset=80):
    
    empty_img = Image.open(self.template_name)
    img_w, img_h= empty_img.size

    # name
    name = self.attendee_name
    n_height = name_height
    font = ImageFont.truetype(font_style, name_size)
    font_w, font_h = font.getsize(name)
    name_h_centre = img_w/2 - font_w/2 + name_offset

    # project
    project = self.project_name
    project_font_size = project_size
    p_height = project_height
    project_font = ImageFont.truetype(font_style, project_font_size)
    p_font_w, p_font_h = font.getsize(project)
    project_h_centre = img_w/2 - p_font_w/2 + project_offset

    # name
    image_editable = ImageDraw.Draw(empty_img)
    image_editable.text((name_h_centre,n_height), name, name_color, font=font)
    empty_img.save(file_name)

    # project
    image_w_name = Image.open(file_name)
    image_editable_p = ImageDraw.Draw(image_w_name)
    image_editable_p.text((project_h_centre,p_height), project, project_color, font=project_font)
    image_w_name.save(file_name)