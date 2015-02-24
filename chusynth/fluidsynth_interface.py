__author__ = 'pakitochus'
import fluidsynth

fs = fluidsynth.Synth()
fs.start(driver="alsa")

sfid = fs.sfload("/usr/share/sounds/sf2/FluidR3_GM.sf2")
fs.program_select(0, sfid, 0, 0)
