import instaloader

mod = instaloader.Instaloader()




while (True):
    mod.download_profile(input('target Name: '), profile_pic_only=True)

