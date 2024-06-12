from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, vfx
from dictionnaire import PATH_DICT

def word_to_clip(parsed):
    clip_list = list()
    for i in parsed:
        for j in i:
            clip_list.append(PATH_DICT[j])
    return clip_list


def concatenate_sign_clip(parsed):
    clip_list = word_to_clip(parsed)

    clips = [VideoFileClip(file) for file in clip_list]

    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("./Files/video/overlay.mp4", codec="libx264")
    

def clip_and_overlay():
    main = VideoFileClip("./Files/video/video.mp4")
    overlay = VideoFileClip("./Files/video/overlay.mp4")

    ratio = overlay.duration/main.duration
    overlay = overlay.fx(vfx.speedx,ratio)
    #Parametre a changer pour modifier la taille de l'overlay
    overlay = overlay.resize(height=200)

    #Parametre a changer pour modifier l'endroit de l'overlay
    overlay_position = (100, 100) 
    
    overlay_position = (main.size[0] - overlay.size[0],main.size[1] - overlay.size[1])
    
    final = CompositeVideoClip([main, overlay.set_pos(overlay_position)])
    final.write_videofile("./Files/video/video_finale.mp4", codec="libx264")


def parsed_to_clip(parsed):
    concatenate_sign_clip(parsed)
    clip_and_overlay()    


parsed_to_clip([['bonjour'], ['ça va'], ['oui'], ['super', 'et toi'], ['fatigué'], ['ah bon'], ['pourquoi'], ['nuit', 'dernier', 'dormir', 'mal'], ['désolé'], ['que fais-tu'], ['samedi', 'prochain'], ['week-end', 'aimer', 'balader', 'famille'], ['restaurant', 'aller', 'ami'], ['et toi'], ["j'adore", 'aller', 'courir', 'parc', 'fin', 'journée'], ["m'accompagne"], ["t'accompagne"]])
