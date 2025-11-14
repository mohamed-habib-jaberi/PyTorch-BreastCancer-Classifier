# Lab for 040-010-deployment-options

# 🍎 Environment Setup — macOS (Apple Silicon M3/M4)

This project was developed and tested on a **MacBook Pro M4 (Apple Silicon)** running macOS.  
Because Apple Silicon uses an **ARM64 architecture**, some Python libraries (like PyTorch and ONNX) require specific setup steps for compatibility.  
This guide documents the **exact steps** used to configure and validate a fully functional deep learning environment.

---

## ⚙️ 1. Install Python 3.11 (Apple Silicon)

We recommend using **Python 3.11** since it provides the best balance of performance and compatibility with modern ML frameworks.

Install Python using **Homebrew**:

```bash
brew install python@3.11
```

### ✅ Then verify the installation

Check that Python was correctly installed and is accessible from your shell:

```bash
/opt/homebrew/bin/python3.11 --version
```

Expected output:
```
Python 3.11.x
```

If you get `command not found: python3.11`, make sure your Homebrew path is correctly set:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
source ~/.zprofile
```

---

## 🧩 2. Create and Activate a Virtual Environment

To isolate your dependencies and ensure reproducibility, create a virtual environment in your project root.

```bash
/opt/homebrew/bin/python3.11 -m venv .venv311
```

Then activate it:

```bash
source .venv311/bin/activate
```

You should now see `(.venv311)` at the start of your terminal prompt.

---

### 🔍 Verify that your virtual environment is active

Run:
```bash
which python
```

Expected output:
```
/Users/<username>/Downloads/PyTorch-main/.venv311/bin/python
```

💡 This confirms that you’re using the Python binary inside your virtual environment — not the global one.

---

## 📦 3. Upgrade pip and Core Tools

Before installing any dependencies, always make sure `pip`, `setuptools`, and `wheel` are updated to avoid installation issues.

```bash
pip install -U pip setuptools wheel
```

---

## 🧠 4. Install ONNX and ONNX Runtime (Apple Silicon)

**ONNX** is a universal open format for machine learning models.  
**ONNX Runtime** runs those models efficiently on CPUs and GPUs.

First, try installing both packages normally:

```bash
pip install onnx onnxruntime
```

---

### ⚠️ If you see this error:

```
ERROR: Could not find a version that satisfies the requirement onnxruntime
```

That means Microsoft hasn’t yet published an Apple Silicon (ARM64) wheel for `onnxruntime`.  
You can try the silicon build (if available):

```bash
pip install onnx onnxruntime-silicon
```

If that doesn’t work:
- You can skip ONNX Runtime (PyTorch works fine without it), or  
- Build ONNX Runtime manually from source using CMake (advanced setup).

---

## 🔥 5. Install PyTorch (Apple Silicon Build)

To enable GPU acceleration through Apple’s **Metal Performance Shaders (MPS)**, install the Metal-compatible PyTorch build:

```bash
pip install torch torchvision torchaudio
```

---

### 🔍 Verify GPU availability

Run this command:

```bash
python -c "import torch; print(torch.backends.mps.is_available())"
```

Expected output:
```
True
```

✅ If this prints `True`, PyTorch can use your Mac GPU automatically.

If it prints `False`, reinstall PyTorch or ensure your macOS and Xcode Command Line Tools are up to date.

---

## ⚙️ 6. Install Project Dependencies

After setting up the environment, install all Python dependencies for this project using:

```bash
pip3 install -r requirements.txt
```

This ensures all modules required by the project are installed in your virtual environment.

---

## 🚀 7. Run Setup Script for Deployment Demos

To initialize the environment for deployment options and scripts, run the provided setup shell file:

```bash
bash PyTorch/section_4/demos/040-010-deployment-options/setup.sh
```

This will prepare the necessary files, models, and configurations used in the deployment demonstrations.

---

## 🔍 8. Verify the Complete Setup

Check that PyTorch and ONNX are correctly installed:

```bash
python -c "import torch, onnx; print('✅ PyTorch and ONNX are ready!')"
```

Expected output:
```
✅ PyTorch and ONNX are ready!
```

---

## 🧾 9. Summary of All Commands

Here’s the complete setup sequence for reference:

```bash
# 1️⃣ Install Python 3.11
brew install python@3.11

# 2️⃣ Create and activate a virtual environment
/opt/homebrew/bin/python3.11 -m venv .venv311
source .venv311/bin/activate

# 3️⃣ Upgrade pip and build tools
pip install -U pip setuptools wheel

# 4️⃣ Install ONNX + ONNX Runtime (try standard first)
pip install onnx onnxruntime

# 5️⃣ Install PyTorch with Metal GPU support
pip install torch torchvision torchaudio

# 6️⃣ Install project dependencies
pip3 install -r requirements.txt

# 7️⃣ Run setup script for deployment demos
bash PyTorch/section_4/demos/040-010-deployment-options/setup.sh
```

---

## 💡 Notes and Tips

- Apple Silicon (M1–M4) chips use the **ARM64** architecture — some older libraries may not have prebuilt binaries yet.
- Always install packages **after activating your virtual environment**.
- To deactivate the environment:
  ```bash
  deactivate
  ```
- In **VS Code**, select the environment via  
  `Command Palette → Python: Select Interpreter → .venv311`
- Use MPS (Metal) for GPU acceleration:
  ```bash
  python -c "import torch; print(torch.device('mps'))"
  ```

---

## 🧠 Troubleshooting

| Problem | Likely Cause | Solution |
|----------|---------------|-----------|
| `No matching distribution found for onnxruntime` | Apple Silicon build missing | Try `onnxruntime-silicon` or build from source |
| `zsh: command not found: python3.11` | Homebrew path not added to shell | Run `eval "$(/opt/homebrew/bin/brew shellenv)"` |
| `torch.backends.mps.is_available() == False` | PyTorch not compiled with Metal backend | Reinstall via `pip install torch torchvision torchaudio` |
| `pip install` stuck on building wheels | Xcode Command Line Tools missing | Run `xcode-select --install` |

---

## ✅ Final Verification

After completing all steps, you’ll have a fully working environment supporting:
- PyTorch (CPU + Metal GPU)
- ONNX model export and inference
- Full dependency installation
- Deployment-ready scripts
- Clean virtual environment for reproducibility
- Compatibility with Jupyter, VS Code, and CLI

---

### 🧾 Quick Recap of All Commands

```bash
brew install python@3.11
/opt/homebrew/bin/python3.11 -m venv .venv311
source .venv311/bin/activate
pip install -U pip setuptools wheel
pip install onnx onnxruntime
pip install torch torchvision torchaudio
python -m pip install "numpy<2.0"
pip3 install -r requirements.txt
bash PyTorch/section_4/demos/040-010-deployment-options/setup.sh
python -c "import torch; print(torch.backends.mps.is_available())"
python -c "import torch, onnx; print('✅ PyTorch and ONNX are ready!')"
```

---

### 📚 Recommended Next Step

Once your environment is configured, verify model export to ONNX using:

```bash
python -c "import torch; dummy = torch.randn(1, 3, 224, 224); model = torch.hub.load('pytorch/vision', 'resnet18', pretrained=True); torch.onnx.export(model, dummy, 'resnet18.onnx')"
```

---

🎉 **Your macOS (Apple Silicon) environment is now ready for deep learning, ONNX workflows, and deployment demos!**