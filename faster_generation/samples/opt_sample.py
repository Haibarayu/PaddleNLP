# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from paddlenlp.transformers import GPTLMHeadModel, GPTChineseTokenizer
import paddle

model_name = 'facebook/opt-1.3b'

tokenizer = GPTChineseTokenizer.from_pretrained(model_name)
model = GPTLMHeadModel.from_pretrained(model_name)
model.eval()

inputs = """Question:If x is 2 and y is 5, what is x+y?
Answer: 7
Question: if x is 12 and y is 9, what is x+y?
Answer:21"
Question: if x is 3 and y is 4, what is x+y?"""

inputs_ids = tokenizer([inputs])["input_ids"]
inputs_ids = paddle.to_tensor(inputs_ids, dtype='int64').unsqueeze(0)

outputs, _ = model.generate(input_ids=inputs_ids,
                            max_length=10,
                            decode_strategy='greedy_search',
                            use_faster=True)

result = tokenizer.convert_ids_to_string(outputs[0].numpy().tolist())

print("Model input:", inputs)
print("Result:", result)
