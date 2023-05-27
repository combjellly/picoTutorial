import pvleopard

access_key = 'place your access key here'
audio_path = 'place the full name of your audio path/file here'

leopard = pvleopard.create(access_key)

transcript = leopard.process_file(audio_path)

#remove the [0] to print both the trascription and the sequence of words with their accompanying metadata. 
print(transcript[0])