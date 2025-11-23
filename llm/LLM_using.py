from transformers import BertForMaskedLM, BertTokenizer, pipeline

def LLM_using(sequence):
    tokenizer = BertTokenizer.from_pretrained('virtual-human-chc/prot_bert_bfd', do_lower_case=False )
    model = BertForMaskedLM.from_pretrained('virtual-human-chc/prot_bert_bfd')
    unmasker = pipeline('fill-mask', model=model, tokenizer=tokenizer)
    result_list=list(unmasker(sequence))
    print(result_list[0])
    return result_list[0]['sequence']