#!/usr/bin/env python3
import json, subprocess
PREFERRED=['/generate','/chat','/predict','/respond','/infer','/run']

def run(cmd,timeout=240):
    return subprocess.run(cmd,capture_output=True,text=True,timeout=timeout)

def payload(spec,prompt):
    out={}; setp=False
    for p in spec.get('parameters',[]):
        n=p.get('name',''); l=n.lower(); req=bool(p.get('required',False)); default=p.get('default'); typ=(p.get('type') or {}).get('type')
        if l in {'message','prompt','text','query','input','instruction','user_message'}: out[n]=prompt; setp=True
        elif l in {'chat_history','history','messages'}: out[n]=[]
        elif l in {'max_new_tokens','max_tokens','maximum_new_tokens'}: out[n]=700
        elif l=='temperature': out[n]=0.1
        elif l=='top_p': out[n]=0.9
        elif l=='top_k': out[n]=40
        elif l in {'system','system_prompt'}: out[n]='CEREBRON rigorous falsifier. CLAIM<=EVIDENCE.'
        elif req and default is None:
            if typ=='string' and not setp: out[n]=prompt; setp=True
            else: return None
    return out if setp else None

def extract(raw):
    raw=raw.strip()
    try:
        o=json.loads(raw)
        if isinstance(o,dict):
            for k in ('Response','response','text','output','message'):
                if isinstance(o.get(k),str): return o[k].strip()
    except Exception: pass
    return raw

def invoke(space,prompt):
    i=run(['hf-gradio','info',space],120)
    if i.returncode!=0: return False,'',{'stage':'info','error':(i.stderr or i.stdout)[-1200:]}
    try: api=json.loads(i.stdout)
    except Exception as e: return False,'',{'stage':'decode','error':repr(e)}
    eps=list(api.items()); eps.sort(key=lambda kv:(PREFERRED.index(kv[0]) if kv[0] in PREFERRED else 99,kv[0]))
    errs=[]
    for ep,spec in eps:
        pl=payload(spec,prompt)
        if pl is None: continue
        r=run(['hf-gradio','predict',space,ep,json.dumps(pl,ensure_ascii=False)],240)
        if r.returncode==0 and (r.stdout or '').strip(): return True,extract(r.stdout),{'stage':'predict','endpoint':ep}
        errs.append((r.stderr or r.stdout)[-600:])
    return False,'',{'stage':'predict','error':' | '.join(errs[-3:])}
