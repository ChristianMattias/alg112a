# Original PyTorch code
import torch

class LinearRegressionModel(torch.nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

model = LinearRegressionModel()

criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)


for epoch in range(1000):
  
    inputs = torch.randn(10, 1)
    targets = 3 * inputs + 2
    outputs = model(inputs)
    loss = criterion(outputs, targets)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


import micrograd as mg

class LinearRegressionModelMicrograd:
    def __init__(self):
        self.w = mg.Parameter(0.0)
        self.b = mg.Parameter(0.0)

    def forward(self, x):
        return self.w * x + self.b

model_micrograd = LinearRegressionModelMicrograd()

for epoch in range(1000):
    # Forward pass
    inputs_micrograd = mg.tensor(mg.randn(10, 1))
    targets_micrograd = 3 * inputs_micrograd + 2
    outputs_micrograd = model_micrograd.forward(inputs_micrograd)
    loss_micrograd = mg.mse_loss(outputs_micrograd, targets_micrograd)

    loss_micrograd.backward()

    model_micrograd.w.data -= 0.01 * model_micrograd.w.grad
    model_micrograd.b.data -= 0.01 * model_micrograd.b.grad

    model_micrograd.w.zero_grad()
    model_micrograd.b.zero_grad()

#chatgpt