#!/usr/bin/python3
from ast import Delete
from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import json
import os
import pathlib
from tkinter import *
from random import seed
from random import randint
import PIL
from PIL import Image

seed(1)


path = pathlib.Path().resolve()




class DeforumGuiApp:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=500, width=500)
        frame6 = tk.Frame(toplevel1)
        frame6.configure(height=200, width=200)
        frame2 = tk.Frame(frame6)
        frame2.configure(height=200, width=200)
        frame5 = tk.Frame(frame2)
        self.l_batch_name = tk.Label(frame5)
        self.l_batch_name.configure(cursor="arrow", justify="left", text="batch_name:")
        self.l_batch_name.grid(column=0, row=0, sticky="e")
        self.l_nbatch = tk.Label(frame5)
        self.l_nbatch.configure(text="n_batch:")
        self.l_nbatch.grid(column=0, row=1, sticky="e")
        self.l_prompts = tk.Label(frame5)
        self.l_prompts.configure(text="prompts:")
        self.l_prompts.grid(column=0, row=2, sticky="e")
        self.l_width = tk.Label(frame5)
        self.l_width.configure(text="width:")
        self.l_width.grid(column=0, row=3, sticky="e")
        self.l_height = tk.Label(frame5)
        self.l_height.configure(text="height:")
        self.l_height.grid(column=0, row=4, sticky="e")
        self.l_steps = tk.Label(frame5)
        self.l_steps.configure(text="steps:")
        self.l_steps.grid(column=0, row=5, sticky="e")
        self.l_scale = tk.Label(frame5)
        self.l_scale.configure(text="scale:")
        self.l_scale.grid(column=0, row=6, sticky="e")
        frame5.grid(column=0, row=0)
        
        frame4 = tk.Frame(frame2)
        self.en_batchname = tk.Entry(frame4)
        self.en_batchname.grid(column=0, row=0)
        self.en_batchname.bind("<1>", self.callback, add="")
        
        self.en_nbatch = tk.Entry(frame4)
        self.en_nbatch.grid(column=0, row=1)
        
        self.en_prompts = tk.Entry(frame4)
        self.en_prompts.grid(column=0, row=2)
        
        self.en_width = tk.Entry(frame4)
        self.en_width.grid(column=0, row=3)
        
        self.en_height = tk.Entry(frame4)
        self.en_height.grid(column=0, row=4)
        
        self.en_steps = tk.Entry(frame4)
        self.en_steps.grid(column=0, row=5)
        
        self.en_scale = tk.Entry(frame4)
        self.en_scale.grid(column=0, row=6)
        
        frame4.grid(column=1, row=0)
        frame2.grid(column=0, row=0)
        frame3 = tk.Frame(frame6)
        frame3.configure(height=200, width=200)
        
        self.l_seed = tk.Label(frame3)
        self.l_seed.configure(text="seed:")
        self.l_seed.grid(column=0, row=0, sticky="e")
        self.en_seed = tk.Entry(frame3)
        self.en_seed.grid(column=1, row=0)
        
        self.bt_rnd = tk.Button(frame3)
        self.bt_rnd.configure(text="Randomize")
        self.bt_rnd.grid(column=1, row=2, sticky="ew")
        self.bt_rnd.configure(command=self.bt_rnd_click)
        
        self.l_behavior = tk.Label(frame3)
        self.l_behavior.configure(text="behavior:")
        self.l_behavior.grid(column=0, row=3, sticky="e")
        self.var_behavior = tk.StringVar(value="iter")
        self.val_behavior = ["iter", "fixed", "random"]
        self.om_behavior = tk.OptionMenu(
            frame3, self.var_behavior, *self.val_behavior, command=None
        )
        self.om_behavior.grid(column=1, row=3, sticky="w")
        
        self.l_sampler = tk.Label(frame3)
        self.l_sampler.configure(text="sampler:")
        self.l_sampler.grid(column=0, row=5, sticky="e")
        self.var_sampler = tk.StringVar(value="klms")
        self.val_sampler = [
            "klms",
            "dpm2",
            "dpm2_ancestral",
            "heun",
            "euler",
            "euler_ancestral",
        ]
        self.om_sampler = tk.OptionMenu(
            frame3, self.var_sampler, *self.val_sampler, command=None
        )
        self.om_sampler.grid(column=1, row=5, sticky="w")
        frame3.grid(column=1, row=0)
        frame6.grid(column=0, row=1)
        labelframe1 = tk.LabelFrame(toplevel1)
        labelframe1.configure(height=200, text="init image batching", width=200)
        
        self.cb_useinit_var = IntVar()
        self.cb_useinit = tk.Checkbutton(labelframe1, variable=self.cb_useinit_var)
        self.cb_useinit.grid(column=0, row=1, sticky="n")
        
        self.en_image = tk.Entry(labelframe1)
        self.en_image.configure(width=30)
        self.en_image.grid(column=2, row=1, sticky="n")
        
        self.bt_loadimage = tk.Button(labelframe1)
        self.bt_loadimage.configure(text="load image")
        self.bt_loadimage.grid(column=2, row=0, sticky="s")
        self.bt_loadimage.configure(command=self.bt_loadimage_click)
        
        self.sc_strength = tk.Scale(labelframe1)
        self.var_strength = tk.DoubleVar()
        self.sc_strength.configure(
            cursor="sb_h_double_arrow",
            from_=0,
            orient="horizontal",
            resolution=0.01,
            sliderlength=10,
            takefocus=False,
            to=1,
            variable=self.var_strength,
            )
        self.sc_strength.grid(column=5, row=0)
        
        self.bt_getimage = tk.Button(labelframe1)
        self.bt_getimage.configure(text="get image size")
        self.bt_getimage.grid(column=5, row=1)
        self.bt_getimage.configure(command=self.bt_getimage_click)
        
        label28 = tk.Label(labelframe1)
        label28.configure(text="activate")
        label28.grid(column=0, row=0, sticky="s")
        labelframe1.grid(column=0, pady=10, row=2)
        
        label29 = tk.Label(toplevel1)
        label29.configure(text="GUI for the awesome Deforum Stable Diffusion")
        label29.grid(column=0, row=0)
        labelframe2 = tk.LabelFrame(toplevel1)
        labelframe2.configure(height=150, text="animation_prompts", width=300)
        frame10 = tk.Frame(labelframe2)
        frame10.configure(height=200, width=200)
        self.txt_prompt1 = ScrolledText(frame10)
        self.txt_prompt1.configure(height=1, width=35, wrap="word")
        self.txt_prompt1.grid(column=1, row=1, sticky="w")
        self.en_frame1 = tk.Entry(frame10)
        self.en_frame1.configure(width=5)
        self.en_frame1.grid(column=0, row=1, sticky="e")
        label31 = tk.Label(frame10)
        label31.configure(text="frame")
        label31.grid(column=0, row=0)
        label32 = tk.Label(frame10)
        label32.configure(text="prompt")
        label32.grid(column=1, row=0)
        frame10.grid(column=0, row=2)
        frame11 = tk.Frame(labelframe2)
        frame11.configure(height=200, width=200)
        self.txt_prompt2 = ScrolledText(frame11)
        self.txt_prompt2.configure(height=1, width=35, wrap="word")
        self.txt_prompt2.grid(column=1, row=1, sticky="w")
        self.en_frame2 = tk.Entry(frame11)
        self.en_frame2.configure(width=5)
        self.en_frame2.grid(column=0, row=1, sticky="e")
        frame11.grid(column=0, row=3)
        frame12 = tk.Frame(labelframe2)
        frame12.configure(height=200, width=200)
        self.txt_prompt3 = ScrolledText(frame12)
        self.txt_prompt3.configure(height=1, width=35, wrap="word")
        self.txt_prompt3.grid(column=1, row=1)
        self.en_frame3 = tk.Entry(frame12)
        self.en_frame3.configure(width=5)
        self.en_frame3.grid(column=0, row=1)
        frame12.grid(column=0, row=4)
        frame13 = tk.Frame(labelframe2)
        frame13.configure(height=200, width=200)
        self.txt_prompt4 = ScrolledText(frame13)
        self.txt_prompt4.configure(height=1, width=35, wrap="word")
        self.txt_prompt4.grid(column=1, row=1)
        self.en_frame4 = tk.Entry(frame13)
        self.en_frame4.configure(width=5)
        self.en_frame4.grid(column=0, row=1)
        frame13.grid(column=0, row=5)
        frame14 = tk.Frame(labelframe2)
        frame14.configure(height=200, width=200)
        self.txt_prompt5 = ScrolledText(frame14)
        self.txt_prompt5.configure(height=1, width=35, wrap="word")
        self.txt_prompt5.grid(column=1, row=1)
        self.en_frame5 = tk.Entry(frame14)
        self.en_frame5.configure(width=5)
        self.en_frame5.grid(column=0, row=1)
        frame14.grid(column=0, row=6)
        labelframe2.grid(column=0, row=3)
        frame15 = tk.Frame(toplevel1)
        frame15.configure(height=200, width=200)
        self.var_anim = tk.StringVar(value="3D")
        self.val_anim = ["None", "2D", "3D", "Video Input", "Interpolation"]
        self.om_anim = tk.OptionMenu(frame15, self.var_anim, *self.val_anim, command=None)
        self.om_anim.grid(column=0, row=0, sticky="w")
        self.l_maxframes = tk.Label(frame15)
        self.l_maxframes.configure(text="max_frames:")
        self.l_maxframes.grid(column=1, row=0, sticky="e")
        self.en_maxframes = tk.Entry(frame15)
        self.en_maxframes.configure(width=5)
        self.en_maxframes.grid(column=2, row=0)
        self.l_cadence = tk.Label(frame15)
        self.l_cadence.configure(text="cadence:")
        self.l_cadence.grid(column=3, row=0, sticky="e")
        self.en_cadence = tk.Entry(frame15)
        self.en_cadence.configure(width=5)
        self.en_cadence.grid(column=4, row=0)
        self.l_border = tk.Label(frame15)
        self.l_border.configure(text="border:")
        self.l_border.grid(column=5, row=0, sticky="e")
        self.var_border = tk.StringVar(value="warp")
        self.val_border = ["warp", "replicate"]
        self.om_border = tk.OptionMenu(
            frame15, self.var_border, *self.val_border, command=None
        )
        self.om_border.grid(column=7, row=0)
        frame15.grid(column=0, pady=10, row=4, sticky="ew")
        labelframe3 = tk.LabelFrame(toplevel1)
        labelframe3.configure(height=200, text="translation", width=200)
        
        self.l_transx1 = tk.Label(labelframe3)
        self.l_transx1.configure(text="x:")
        self.l_transx1.grid(column=0, padx=0, pady=0, row=0, sticky="e")
        self.en_transx1 = tk.Entry(labelframe3)
        self.en_transx1.configure(width=15)
        self.en_transx1.grid(column=1, row=0)
        
        self.l_transy1 = tk.Label(labelframe3)
        self.l_transy1.configure(text="y:")
        self.l_transy1.grid(column=2, row=0)
        self.en_transy1 = tk.Entry(labelframe3)
        self.en_transy1.configure(width=15)
        self.en_transy1.grid(column=3, row=0)
        
        self.l_transz1 = tk.Label(labelframe3)
        self.l_transz1.configure(text="z:")
        self.l_transz1.grid(column=4, row=0)
        self.en_transz1 = tk.Entry(labelframe3)
        self.en_transz1.configure(width=15)
        self.en_transz1.grid(column=5, padx=0, row=0)
        
        labelframe3.grid(column=0, row=6)
        labelframe3.rowconfigure("all", pad=15)
        labelframe3.columnconfigure("all", pad=5)
        
        labelframe5 = tk.LabelFrame(toplevel1)
        labelframe5.configure(height=200, text="rotation 3d", width=200)
        
        self.l_rotx1 = tk.Label(labelframe5)
        self.l_rotx1.configure(text="x:")
        self.l_rotx1.grid(column=0, padx=0, pady=0, row=0, sticky="e")
        self.en_rotx1 = tk.Entry(labelframe5)
        self.en_rotx1.configure(width=15)
        self.en_rotx1.grid(column=1, row=0)
        
        self.l_roty1 = tk.Label(labelframe5)
        self.l_roty1.configure(text="y:")
        self.l_roty1.grid(column=2, row=0)
        self.en_roty1 = tk.Entry(labelframe5)
        self.en_roty1.configure(width=15)
        self.en_roty1.grid(column=3, row=0)
        
        self.l_rotz1 = tk.Label(labelframe5)
        self.l_rotz1.configure(text="z:")
        self.l_rotz1.grid(column=4, row=0)
        self.en_rotz1 = tk.Entry(labelframe5)
        self.en_rotz1.configure(width=15)
        self.en_rotz1.grid(column=5, padx=0, row=0)
        
        labelframe5.grid(column=0, row=7)
        labelframe5.rowconfigure("all", pad=15)
        labelframe5.columnconfigure("all", pad=5)
        labelframe6 = tk.LabelFrame(toplevel1)
        labelframe6.configure(height=200, text="some more stuff", width=200)
        
        self.cb_interpolate_var = IntVar()
        self.cb_interpolate = tk.Checkbutton(labelframe6, variable=self.cb_interpolate_var)
        self.cb_interpolate.configure(justify="left", text="interpolate_key_frames")
        self.cb_interpolate.grid(column=0, row=0, sticky="w")
        self.en_interpolate = tk.Entry(labelframe6)
        self.en_interpolate.grid(column=2, row=0)
       
        self.cb_restimestring_var = IntVar()
        self.cb_restimestring = tk.Checkbutton(labelframe6, variable=self.cb_restimestring_var)
        self.cb_restimestring.configure(justify="left", text="resume_from_timestring")
        self.cb_restimestring.grid(column=0, row=1, sticky="w")
        self.en_restimestring = tk.Entry(labelframe6)
        self.en_restimestring.grid(column=2, row=1)
        
        labelframe6.grid(column=0, row=8)
        
        frame17 = tk.Frame(toplevel1)
        frame17.configure(height=200, width=200)
        self.bt_load = tk.Button(frame17)
        self.bt_load.configure(text="LOAD")
        self.bt_load.grid(column=0, row=0)
        self.bt_load.configure(command=self.bt_load_click)
        self.bt_save = tk.Button(frame17)
        self.bt_save.configure(text="SAVE")
        self.bt_save.grid(column=1, row=0)
        self.bt_save.configure(command=self.bt_save_click)
        self.bt_info = tk.Button(frame17)
        self.bt_info.configure(text="info")
        self.bt_info.grid(column=5, row=0)
        self.bt_info.configure(command=self.bt_info_click)
        frame17.grid(column=0, row=9)
        toplevel1.grid_anchor("center")

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def callback(self, event=None):
        pass



    def bt_getimage_click(self):
        with Image.open(self.en_image.get()) as img:
            wid, hgt = img.size

        self.en_width.delete(0, tk.END)
        self.en_width.insert(tk.INSERT, wid)
        
        self.en_height.delete(0, tk.END)
        self.en_height.insert(tk.INSERT, hgt)




    def bt_rnd_click(self):
        self.en_seed.delete(0, tk.END)
        for _ in range(1):
	        self.en_seed.insert(tk.INSERT, randint(0, 999999999))



    def bt_loadimage_click(self):
        DeforumGuiApp.filename_image = filedialog.askopenfilename(initialdir=path, title="Select source image", filetypes=[("image files", "*.jpg *.png")])
        
        rel_path_filename = os.path.abspath(DeforumGuiApp.filename_image)
        rel_path_image = os.path.relpath(rel_path_filename, path)
        self.en_image.delete(0, tk.END)
        self.en_image.insert(tk.INSERT, "./" + rel_path_image.replace("\\", "/"))




    def bt_load_click(self):
        DeforumGuiApp.filename_load = filedialog.askopenfilename(initialdir=path, title="Select config file", filetypes=[("text files", "*.txt")])

        with open(DeforumGuiApp.filename_load) as f:
            json_data = json.load(f)
        
        self.en_batchname.delete(0, tk.END)
        self.en_batchname.insert(tk.INSERT, json_data['batch_name'])
        
        self.en_nbatch.delete(0, tk.END)
        self.en_nbatch.insert(tk.INSERT, json_data['n_batch'])
        
        self.en_prompts.delete(0, tk.END)
        self.en_prompts.insert(tk.INSERT, json_data['prompts'])
        
        self.en_width.delete(0, tk.END)
        self.en_width.insert(tk.INSERT, json_data['width'])
        
        self.en_height.delete(0, tk.END)
        self.en_height.insert(tk.INSERT, json_data['height'])
        
        self.en_seed.delete(0, tk.END)
        self.en_seed.insert(tk.INSERT, json_data['seed'])
        
        self.en_steps.delete(0, tk.END)
        self.en_steps.insert(tk.INSERT, json_data['steps'])

        self.en_scale.delete(0, tk.END)
        self.en_scale.insert(tk.INSERT, json_data['scale'])

        self.en_image.delete(0, tk.END)
        self.en_image.insert(tk.INSERT, json_data['init_image'])

        self.en_maxframes.delete(0, tk.END)
        self.en_maxframes.insert(tk.INSERT, json_data['max_frames'])       

        self.en_cadence.delete(0, tk.END)
        self.en_cadence.insert(tk.INSERT, json_data['diffusion_cadence'])       

        self.en_interpolate.delete(0, tk.END)
        self.en_interpolate.insert(tk.INSERT, json_data['interpolate_x_frames'])       

        self.en_restimestring.delete(0, tk.END)
        self.en_restimestring.insert(tk.INSERT, json_data['resume_timestring'])  

        self.en_transx1.delete(0, tk.END)
        self.en_transx1.insert(tk.INSERT, json_data['translation_x']) 

        self.en_transy1.delete(0, tk.END)
        self.en_transy1.insert(tk.INSERT, json_data['translation_y']) 

        self.en_transz1.delete(0, tk.END)
        self.en_transz1.insert(tk.INSERT, json_data['translation_z']) 

        self.en_rotx1.delete(0, tk.END)
        self.en_rotx1.insert(tk.INSERT, json_data['rotation_3d_x'])

        self.en_roty1.delete(0, tk.END)
        self.en_roty1.insert(tk.INSERT, json_data['rotation_3d_y'])

        self.en_rotz1.delete(0, tk.END)
        self.en_rotz1.insert(tk.INSERT, json_data['rotation_3d_z'])


        self.anim_promts_keys = list(json_data['animation_prompts'])

        if len(self.anim_promts_keys) >= 1:
            self.en_frame1.delete(0, tk.END)
            self.en_frame1.insert(tk.INSERT, self.anim_promts_keys[0]) 
        
            self.txt_prompt1.delete('1.0', tk.END)
            self.txt_prompt1.insert(tk.INSERT, json_data['animation_prompts'][self.anim_promts_keys[0]])


        if len(self.anim_promts_keys) >= 2:       
            self.en_frame2.delete(0, tk.END)
            self.en_frame2.insert(tk.INSERT, self.anim_promts_keys[1]) 

            self.txt_prompt2.delete('1.0', tk.END)
            self.txt_prompt2.insert(tk.INSERT, json_data['animation_prompts'][self.anim_promts_keys[1]])


        if len(self.anim_promts_keys) >= 3:
            self.en_frame3.delete(0, tk.END)
            self.en_frame3.insert(tk.INSERT, self.anim_promts_keys[2]) 

            self.txt_prompt3.delete('1.0', tk.END)
            self.txt_prompt3.insert(tk.INSERT, json_data['animation_prompts'][self.anim_promts_keys[2]])


        if len(self.anim_promts_keys) >= 4:
            self.en_frame4.delete(0, tk.END)
            self.en_frame4.insert(tk.INSERT, self.anim_promts_keys[3]) 

            self.txt_prompt4.delete('1.0', tk.END)
            self.txt_prompt4.insert(tk.INSERT, json_data['animation_prompts'][self.anim_promts_keys[3]])


        if len(self.anim_promts_keys) >= 5:
            self.en_frame5.delete(0, tk.END)
            self.en_frame5.insert(tk.INSERT, self.anim_promts_keys[4]) 

            self.txt_prompt5.delete('1.0', tk.END)
            self.txt_prompt5.insert(tk.INSERT, json_data['animation_prompts'][self.anim_promts_keys[4]])


        if json_data['use_init'] == True:
            self.cb_useinit.select()
        elif json_data['use_init'] == False:
            self.cb_useinit.deselect()

        if json_data['interpolate_key_frames'] == True:
            self.cb_interpolate.select()
        elif json_data['interpolate_key_frames'] == False:
            self.cb_interpolate.deselect()

        if json_data['resume_from_timestring'] == True:
            self.cb_restimestring.select()
        elif json_data['resume_from_timestring'] == False:
            self.cb_restimestring.deselect()

        index_anim = self.val_anim.index(json_data['animation_mode'])
        self.var_anim.set(self.val_anim[index_anim])

        index_beh = self.val_behavior.index(json_data['seed_behavior'])
        self.var_behavior.set(self.val_behavior[index_beh])

        index_sampler = self.val_sampler.index(json_data['sampler'])
        self.var_sampler.set(self.val_sampler[index_sampler])

        index_border = self.val_border.index(json_data['border'])
        self.var_border.set(self.val_border[index_border])

        self.var_strength.set(json_data['strength'])



    def bt_save_click(self):

        dic_anim_promt = {}
        if len(self.en_frame1.get()) != 0:
            dic_anim_promt[self.en_frame1.get()] = self.txt_prompt1.get("1.0",'end-1c')
        if len(self.en_frame2.get()) != 0:
            dic_anim_promt[self.en_frame2.get()] = self.txt_prompt2.get("1.0",'end-1c')      
        if len(self.en_frame3.get()) != 0:
            dic_anim_promt[self.en_frame3.get()] = self.txt_prompt3.get("1.0",'end-1c')
        if len(self.en_frame4.get()) != 0:
            dic_anim_promt[self.en_frame4.get()] = self.txt_prompt4.get("1.0",'end-1c')
        if len(self.en_frame5.get()) != 0:
            dic_anim_promt[self.en_frame5.get()] = self.txt_prompt5.get("1.0",'end-1c')

        dictionary = {
            "batch_name":self.en_batchname.get(),
            "n_batch":int(self.en_nbatch.get()),
            "prompts":self.en_prompts.get(),
            "width":int(self.en_width.get()),
            "height":int(self.en_height.get()),
            "seed":int(self.en_seed.get()),
            "seed_behavior":self.var_behavior.get(),
            "sampler":self.var_sampler.get(),
            "steps":int(self.en_steps.get()),
            "scale":int(self.en_scale.get()),
            "ddim_eta":0.0,
            "filename_format":"{timestring}_{index}_{prompt}.png",
            "use_init":bool(self.cb_useinit_var.get()),
            "init_image":self.en_image.get(),
            "strength":self.var_strength.get(),
            "use_mask":False,
            "use_alpha_as_mask":False,
            "invert_mask":False,
            "mask_file":"",
            "animation_prompts": dic_anim_promt,
            "animation_mode":self.var_anim.get(),
            "max_frames":int(self.en_maxframes.get()),
            "diffusion_cadence":self.en_cadence.get(),
            "border":self.var_border.get(),
            "angle":"0:(0)",
            "zoom":"0:(0)",
            "translation_x":self.en_transx1.get(),
            "translation_y":self.en_transy1.get(),
            "translation_z":self.en_transz1.get(),
            "rotation_3d_x":self.en_rotx1.get(),
            "rotation_3d_y":self.en_roty1.get(),
            "rotation_3d_z":self.en_rotz1.get(),
            "noise_schedule":"0:(0.02)",
            "strength_schedule":"0:(0.65)",
            "contrast_schedule":"0:(1.0)",
            "color_coherence":"Match Frame 0 LAB",
            "use_depth_warping":True,
            "midas_weight":0.3,
            "near_plane":200,
            "far_plane":10000,
            "fov":40,
            "padding_mode":"border",
            "sampling_mode":"bicubic",
            "save_depth_maps":False,
            "video_init_path":"./input/video_in.mp4",
            "extract_nth_frame":1,
            "interpolate_key_frames":bool(self.cb_interpolate_var.get()),
            "interpolate_x_frames":int(self.en_interpolate.get()),
            "resume_from_timestring":bool(self.cb_restimestring_var.get()),
            "resume_timestring":self.en_restimestring.get()
        }

        with open(DeforumGuiApp.filename_load, "w") as outfile:
            json.dump(dictionary, outfile, default=lambda o: o.__dict__, separators=(',', ':'), indent=4)


    def bt_info_click(self):
        pass


if __name__ == "__main__":
    app = DeforumGuiApp()
    app.run()
