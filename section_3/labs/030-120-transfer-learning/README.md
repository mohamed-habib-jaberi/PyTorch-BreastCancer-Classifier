# Lab for 030-120-transfer-learning




## 🧩 Conclusion

In this project, we explored **two transfer learning approaches** using different pre-trained models — **ResNet18** and **MobileNetV3** — to understand their trade-offs and performance characteristics.

---

### 🧠 ResNet18 Model (Fine-Tuning)

**Approach**
- Modified the final fully connected layer to output **2 classes** instead of 1000  
- Kept **all layers trainable** (full fine-tuning)  
- Used a **StepLR** scheduler to gradually reduce the learning rate  
- Optimized with **SGD** and momentum  

**✅ Benefits**
- Better performance potential through full model adaptation  
- Learns **task-specific features** rather than generic ones  
- Offers more **flexibility across domains**  
- Yields better results when the **target task differs** from the source task  

---

### ⚡ MobileNetV3 Model (Feature Extraction)

**Approach**
- Modified the classifier’s final layer for **2 output classes**  
- **Froze all layers** except the final classification layer  
- Used an **ExponentialLR** scheduler for learning rate decay  
- Trained **only the final layer’s parameters**  

**✅ Benefits**
- Much **faster training time**  
- Requires **fewer computational resources**  
- Works better for **small datasets**  
- Helps **prevent overfitting**  
- Provides a **more stable training process**  

---

### ⚖️ Comparison

| Aspect | Fine-Tuning (ResNet18) | Feature Extraction (MobileNetV3) |
|:------|:------------------------|:--------------------------------|
| **Trainable layers** | All | Final only |
| **Training speed** | Slower | Faster |
| **Compute needs** | Higher | Lower |
| **Overfitting risk** | Higher | Lower |
| **Best for** | Complex or domain-specific tasks | Small datasets or quick adaptation |

---

### 🏁 Summary

Both are valid **transfer learning** strategies:  
- **Fine-tuning** delivers stronger adaptation and potentially higher accuracy, at the cost of longer training and higher compute needs.  
- **Feature extraction** offers efficiency and stability, especially when data is limited or rapid prototyping is needed.

### 🚀 Run the Setup Script

To reproduce the environment and dependencies used for training, simply run:

```bash
bash PyTorch/section_3/demos/030-120-transfer-learning/setup.sh