# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:40:54 2023

@author: jugwu
"""
import JGPT_model as jgpt
import torch.nn as nn
import torch.optim as optim
import data_loader as dl
from tqdm import tqdm
import utilities as util
import embedding as emb
import torch
import os
import parameters as para

def log(itr, loss):
    print("writing......")
    full_path = PATH + FILE + "_log.txt"
    if os.path.exists(full_path):
        with open("logs\\" + full_path, 'r',encoding="utf-8") as f:
            lines = f.readlines()
        f.close()
        
        lines[10] = str(loss) + "\n"
        lines[12] = str(int(lines[12]) + itr) + "\n"

        with open("logs\\" + full_path, 'w',encoding="utf-8") as f:
            for line in tqdm(lines):
                f.write(line)
        f.close()
        
    else:      
        lines = []
        lines.append(FILE)
        lines.append("D_model::::")
        lines.append(str(para.d_model))
        lines.append("Seq_length:")
        lines.append(str(para.max_seq_length))
        lines.append("Vocab_Size:")
        lines.append(str(para.vocab_size))
        lines.append("Encoders:::")
        lines.append(str(para.num_encoders))
        lines.append("Loss:::::::")
        lines.append(str(loss))
        lines.append("Iteration::")
        lines.append(str(itr))
        
        with open("logs\\" + full_path, 'w',encoding="utf-8") as f:
            for line in tqdm(lines):
                f.write(line)
                f.write("\n")
        f.close()
        
    return

def train(num : int = 10, base_model = None, length : int = 1):
    
    if base_model !=None:
        model=base_model
    else:
        model = jgpt.J_GPT()
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters())#, lr=0.01)
    #print("yo")
    
    data = util.load_sentences("clean3")
    tags, vectors = emb.load("memebed5")
    
    enc_inputs, dec_inputs, target_batch = dl.sample(data, tags, vectors, length)
    aloss = 0
    
    print("TRAIN::::")
    for epoch in range(num):
        aloss = 0
        enc_inputs, dec_inputs, target_batch = dl.sample(data, tags, vectors,length)
        counter = 0
        for outs, targs in tqdm(zip(dec_inputs, target_batch)):
            optimizer.zero_grad()
            counter +=1
            outputs = model(' '.join(enc_inputs), ' '.join(outs), counter)
            loss = criterion(outputs, targs)
            aloss+=loss

            loss.backward()
            optimizer.step()
        AV_loss = aloss/target_batch.shape[0]
        print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.12f}'.format(AV_loss))
        
    print("EVAL::::")
    outputs = model.evaluate(' '.join(enc_inputs), ' '.join(outs))
    print(outputs)
    log(num, AV_loss)
    return model

FILE = "TRANSFORMERMODEL3"
PATH = "transformers\\"
FULL_PATH = PATH + FILE + ".pt"
def main():
    model = jgpt.J_GPT()
    
    model.load_state_dict(torch.load(FULL_PATH))
    model = train(20, base_model=model)
    torch.save(model.state_dict(), FULL_PATH)
            
    print("TEST::::")
    text = 'hi how are you q'
    model.talk(text, 8)
    #print()
    #model.talk(text, 50)

    return 0 

if __name__=="__main__":
    main()