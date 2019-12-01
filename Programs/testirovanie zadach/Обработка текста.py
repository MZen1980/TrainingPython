def process(sentences):

    c = []
    for i in sentences:
        a = ''.join(i).split()
        b = list(filter(lambda x: x.isalpha(), a))
        c.append(' '.join(b))
        # print(c)

        result_pr = c
        return result_pr

texts = [
    "Space is the boundless 3-dimensional 42 extent in which objects " \
    "and events have relative 523 position and direction. Physical space " \
    "is often conceived in three linear dimensions, although modern " \
    "physicists usually consider 42 512515 it, with time, to be part of a boundless " \
    "four-dimensional continuum22 known as spacetime. The concept of space is " \
    "considered to b42e of fun*damental importance to an understanding of " \
    "the physical universe. However,{ disagreement continues between philosophers " \
    "over whether it is itself an entity, a relat[[[ionship between entities, " \
    "or part of a conceptual framework. ",
    "Debates concern,,ing the nature, essence and the mode of existence of " \
    "space date back to antiq{{{uity; namely, to treatises like the Timaeus " \
    "of Plato, or Socrates in his reflections on what the Greeks called " \
    "kh?ra (i.e. \fspace'), or in the Physics of Aristotle (Book IV, Delta) " \
    "in the definition of top53253os (i.e. place), or in the later " \
    "'geometrical conception of place' as 'space qua extension' in " \
    "the Discourse on Place (Qawl fi al-Makan) of the 11th-century " \
    "Arab polymath Alhazen.[2] Many of these classical philosophical " \
    "questions were discussed in th<>e Renaissance and then reformulated " \
    "in the 17th century, particularl**y during the early development of " \
    "classical mechanics. In Isaac Newton's view, space was absolute—in " \
    "the sense that it existed permanently and independently of whether there was any matter in the space."
]

result = [
    'Space is the boundless extent in which objects and events have relative position and Physical space is often conceived in three linear although modern physicists usually consider with to be part of a boundless known as The concept of space is considered to of importance to an understanding of the physical disagreement continues between philosophers over whether it is itself an a between or part of a conceptual',
    'Debates the essence and the mode of existence of space date back to to treatises like the Timaeus of or Socrates in his reflections on what the Greeks called or in the Physics of Aristotle in the definition of or in the later conception of as qua in the Discourse on Place fi of the Arab polymath Many of these classical philosophical questions were discussed in Renaissance and then reformulated in the during the early development of classical In Isaac space was the sense that it existed permanently and independently of whether there was any matter in the']


def Test(texts_test, result_test):
    if process(texts_test) == result_test:
        print("Задание успешно выполнено!")
    else:
        print("Ошибка в функции")


Test(texts, result)
# c = []
# for i in texts:
#     a = ''.join(i).split()
#     b = list(filter(lambda x: x.isalpha(), a))
#     c.append(' '.join(b))
#     print(c)
