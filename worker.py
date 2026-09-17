import json, os, pathlib, datetime

ROLE = os.environ.get('ROLE','UNKNOWN_ROLE')
QUESTION = os.environ.get('QUESTION','Analyze language and culture transfer rigorously.')
OUT = pathlib.Path('artifacts')
OUT.mkdir(exist_ok=True)

record = {
    'farm': 29,
    'domain': 'language-culture',
    'role': ROLE,
    'question': QUESTION,
    'status': 'UNREVIEWED_EXTERNAL_AGENT_OUTPUT',
    'timestamp_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'rules': [
        'CLAIM<=EVIDENCE','DESCRIPTION!=VALUE_JUDGMENT','INTERPRETATION!=FACT',
        'CORPUS!=POPULATION','CONTEXT_EXPLICIT','PROVENANCE_REQUIRED',
        'CULTURAL_VARIATION_EXPLICIT','UNKNOWN_REMAINS_UNKNOWN'
    ],
    'output': f'Role {ROLE}: produce a structured evidence-aware analysis, identify assumptions, ambiguities, cultural context, counterexamples, uncertainty, and verification needs.'
}

(OUT / f'{ROLE}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(record, ensure_ascii=False))
