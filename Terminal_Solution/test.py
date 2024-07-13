from pathlib import Path
from playsound import playsound

SCRIPT_DIR = Path(__file__).parent
RINGTONE = SCRIPT_DIR / 'chill_Ringtone.mp3'

playsound(str(RINGTONE))
