import numpy as np

#余弦相似度的计算
def Get_cosine_similarity(vector1,vector2):
    """
    在NLP中往往会计算两个句子的相似度，首先要将二者转化为向量形式
    :param vector1: 输入向量1
    :param vector2: 输入向量2
    :return: 输出为向量1与向量2的余弦相似度
    """
    #将向量1，2转化为numpy向量

    np_vector1 = np.array(vector1)
    np_vector2 = np.array(vector2)

    #计算余弦相似度的分子

    cosine_numerator = np.sum(np.multiply(np_vector1,np_vector2))  #向量元素对应相乘之后取和

    #计算余弦相似度的分母

    cosine_denominator = np.multiply(np.sqrt(np.sum(np.square(np_vector1))),np.sqrt(np.sum(np.square(np_vector2))))  #两个向量元素平方取和开方结果相乘

    #分子/分母得到余弦相似度

    return cosine_numerator/cosine_denominator

#广义Jaccard相似系数的计算:狭义的jaccard相关系数由数值0，1的二值型特征变量计算得来
def Get_jaccard_similarity(vector1,vector2):
    """
    在NLP中往往会计算两个句子的相似度，首先要将二者转化为向量形式
    :param vector1: 输入向量1
    :param vector2: 输入向量2
    :return: 输出为向量1与向量2的广义Jaccard相似系数
    """
    # 将向量1，2转化为numpy向量

    np_vector1 = np.array(vector1)
    np_vector2 = np.array(vector2)

    #计算Jaccard相似系数的分子

    jaccard_numerator = np.sum(np.multiply(np_vector1,np_vector2))  #向量元素对应相乘之后取和
    print(jaccard_numerator)

    #计算Jaccard相关系数的分母
    jaccard_denominator = np.sqrt(np.sum(np.square(np_vector1)))+np.sqrt(np.sum(np.square(np_vector2)))-jaccard_numerator #两向量元素平方之和开方之后去和减去分子

    #分子/分母得到Jaccard相关系数
    return jaccard_numerator/jaccard_denominator

# 测试
if __name__ == "__main__":
    a = [1,2,3,5,2]
    b = [2,5,6,2,7]
    print(Get_cosine_similarity(a,b))
    print(Get_jaccard_similarity(a,b)) #小于0是什么情况？