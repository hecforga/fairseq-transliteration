import os
from argparse import Namespace

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
UPLOADS_DEFAULT_DEST = os.getcwd()
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'doc','docx'])
DEBUG = True

SECRET_KEY = 'RandomKey'
MAIL_SERVER =  'smtp.gmail.com'
BASE_HOST_NAME = "0.0.0.0"


base_args = Namespace(beam=5, buffer_size=0, cpu=False, data='data-bin/translit_la_hy', fp16=False, gen_subset='test', left_pad_source='True',
left_pad_target='False', lenpen=1, log_format=None, log_interval=1000, max_len_a=0, max_len_b=200, max_sentences=None,
 max_source_positions=1024, max_target_positions=1024, max_tokens=None, min_len=1, model_overrides='{}', nbest=1, no_beamable_mm=False,
 no_early_stop=False, no_progress_bar=False, num_shards=1, path='checkpoints/fconv/checkpoint_best.pt',
 prefix_size=0, print_alignment=False, quiet=False, raw_text=False, remove_bpe=None, replace_unk=None, sampling=False,
 sampling_temperature=1, sampling_topk=-1, score_reference=False, seed=1, shard_id=0, skip_invalid_size_inputs_valid_test=False,
 source_lang=None, target_lang=None, task='translation', unkpen=0, unnormalized=False)
