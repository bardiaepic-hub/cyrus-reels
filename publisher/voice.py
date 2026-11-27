"""Turns every tts/requests/*.json without a matching tts/out/*.wav into audio with Chatterbox."""
import glob, json, os
import torch, torchaudio
from chatterbox.tts import ChatterboxTTS

model = None
for req in sorted(glob.glob("tts/requests/*.json")):
    name = os.path.splitext(os.path.basename(req))[0]
    out = f"tts/out/{name}.wav"
    if os.path.exists(out):
        continue
    if model is None:
        model = ChatterboxTTS.from_pretrained(device="cpu")
    spec = json.load(open(req))
    voice = spec.get("voice")
    parts = []
    for ln in spec["lines"]:
        wav = model.generate(ln["text"], audio_prompt_path=voice if voice and os.path.exists(voice) else None,
                             exaggeration=ln.get("exaggeration", spec.get("exaggeration", 0.6)),
                             cfg_weight=ln.get("cfg", spec.get("cfg", 0.4)))
        parts += [wav, torch.zeros(1, int(model.sr * ln.get("pause", 0.3)))]
    os.makedirs("tts/out", exist_ok=True)
    torchaudio.save(out, torch.cat(parts, dim=1), model.sr)
    print("made", out)
