import torch

Data_Path = "/home/yangz/sentiment_analyse"
learning_rate = 0.01  # 学习率
BATCH_SIZE = 512  # 训练批量
EPOCHS = 2  # 训练轮数
model_path = "./saved_models/"  # 预训练模型路径
DEVICE = torch.device('cuda:7' if torch.cuda.is_available() else 'cpu')
update_w2v = True  # 是否在训练中更新w2v
n_class = 2  # 分类数：分别为pos和neg
vocab_size = 70000  # 词汇表大小
embedding_dim = 50  # 词向量维度
drop_keep_prob = 0.5  # dropout层，参数keep的比例
kernel_num = 64  # 卷积层filter的数量
kernel_size = [3, 4, 5]  # 卷积核的尺寸