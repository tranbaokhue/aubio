import aubio
import numpy as np
import sounddevice as sd

print(f"✅ Aubio version: {aubio.version}")
print(f"✅ NumPy version: {np.__version__}")

# Test onset detector creation
onset = aubio.onset("default", 512, 512, 44100)
print("✅ Onset detector created successfully!")

# Test pitch detector creation  
pitch = aubio.pitch("yin", 2048, 512, 44100)
pitch.set_unit("Hz")
print("✅ Pitch detector created successfully!")

print("\n🎵 Ready for onset and pitch detection!")
