base_ext_tox 		= op('base_hueControl')
version 		    = op('table_version')[0,0].val
reset_color 	    = (0.545, 0.545, 0.545)
save_loc 		    = '../release/base_hueControl.tox'
ext_file 		    = 'hueControlEXT'

destroy_ops         = [ 'svg_icon',
                      'transform1'
                     ]

# save tox
# set version
base_ext_tox.par.Version 					= version

# remove path par for ext
base_ext_tox.op(ext_file).par.file 		= ''

# turn off loading on start
base_ext_tox.op(ext_file).par.loadonstart = False

# remove path for extenral tox
base_ext_tox.par.externaltox 				= ''

# set the color to something neutral
base_ext_tox.color 						= reset_color

# lock the tox for the icon
base_ext_tox.op('null_icon').lock 			= True

# destroy all dev ops
for each in destroy_ops:
    base_ext_tox.op(each).destroy()

# save the tox
base_ext_tox.save(save_loc)