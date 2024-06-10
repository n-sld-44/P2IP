from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip

def word_to_clip(word_list):
    clip_list = list()
    for word in word_list:
        clip_list.append("./Files/Avatar_SignTrad/"+word+".mp4")
    return clip_list


def concatenate_sign_clip(word_list):
    clip_list = word_to_clip(word_list)

    clips = [VideoFileClip(file) for file in clip_list]

    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("./Files/video/overlay.mp4", codec="libx264")

def clip_and_overlay():
    main = VideoFileClip("./Files/video/video.mp4")
    overlay = VideoFileClip("./Files/video/overlay.mp4")

    #Parametre a changer pour modifier la taille de l'overlay
    overlay = overlay.resize(height=50)

    #Parametre a changer pour modifier l'endroit de l'overlay
    overlay_position = (50, 50) 
    """ Pour placer l'overlay en bas à droite
    overlay_position = (main.size[0] - overlay.size[0],main.size[1] - overlay.size[1])
    """
    final = CompositeVideoClip([main, overlay.set_pos(overlay_position)])
    final.write_videofile("video_finale.mp4", codec="libx264")