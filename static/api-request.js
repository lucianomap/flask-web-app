document.addEventListener('DOMContentLoaded', () => {
  const button = document.getElementById('fetch-button');
  const resultDiv = document.getElementById('result');

  button.addEventListener('click', async () => {
    resultDiv.textContent = 'Loading...';

    try {
      const response = await fetch('/data');
      if (!response.ok) throw new Error('Error fetching data! Network response failed.');

      const data = await response.json();
      resultDiv.innerHTML = `
        <h2>${data.title}</h2>
        <p>${data.body}</p>
      `;
    } catch (error) {
      resultDiv.textContent = `Error: ${error.message}`;
    }
  });
});
