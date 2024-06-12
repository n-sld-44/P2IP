from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, vfx

def word_to_clip(word_list):
    clip_list = list()
    for word in word_list:
        clip_list.append("./Files/Avatar_SignTrad/"+word+".mov")
    return clip_list


def concatenate_sign_clip(word_list):
    clip_list = word_to_clip(word_list)

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


concatenate_sign_clip(['salut','ça_va','oui','super','et_toi','être_fatigué','ah_bon','pourquoi','nuit','récemment','dormir','mal','désolé','que_fais_tu','samedi','prochain','week_end','aimer','se_balader','famille','ensemble','aller','restaurant','amis','ensemble','et_toi', 'adorer','aller','courir','journée','fin','parc','accompagner','accompagner_tu'])
clip_and_overlay()
