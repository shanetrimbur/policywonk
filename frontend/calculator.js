const defaultTaxRate = 0.22; // Default tax rate, can be adjusted

function calculateTax(income, taxRate = defaultTaxRate) {
    return income * taxRate;
}

function calculatePolicyCost(inflationRate, bondRate, policyCost) {
    return policyCost * (1 + inflationRate) / (1 + bondRate);
}

document.querySelector("#calculate-btn").addEventListener("click", () => {
    const income = parseFloat(document.querySelector("#income-input").value);
    const tax = calculateTax(income);
    document.querySelector("#result").innerText = `Your tax is: ${tax}`;
});
