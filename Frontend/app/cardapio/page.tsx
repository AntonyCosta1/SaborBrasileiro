async function getMenu() {
  const response = await fetch("http://localhost:8000/menu",
    {cache: "no-store",}
  );

  if (!response.ok) {
    throw new Error("Erro ao buscar o cardápio");
  }

  return response.json();
}
export default async function CardapioPage() {
  const itens = await getMenu();

  return (
    <main>
      <h1>Cardapio do dia</h1>
      <ul>
        {itens.map((item: any) => (
          <li key={item.id}>
            {item.name} - R$ {item.price}
          </li>
        ))}
      </ul>
    </main>
  );
}