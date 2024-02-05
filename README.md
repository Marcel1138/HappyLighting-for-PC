# HappyLighting-for-PC

## Simple Triones LED Control

### Installation:

```bash
sudo pip install trionesControl
sudo pip install tk
```

### Prerequisites:

To control your LED, you need the MAC address of the LED. You can find the MAC address using the following command:

```bash
sudo hcitool lescan
```

### Usage:

Change the MAC address in the code:

```python
if __name__ == "__main__":
    # Connect to the LED 
    device = tc.connect('YOUR MAC HERE!!')  # Use "$ sudo hcitool lescan" to find the MAC
```

### Note:

Currently, you can only turn the lamp on and off and change colors because Triones lacks proper documentation.

## How to Use:

1. Install the required modules.
2. Find the MAC address of your LED using `$ sudo hcitool lescan`.
3. Replace `'YOUR MAC HERE!!'` in the code with the discovered MAC address.
4. Run the script.

## Disclaimer:

This project's functionality is limited due to the lack of proper documentation for Triones.

Feel free to contribute or report issues!
```
