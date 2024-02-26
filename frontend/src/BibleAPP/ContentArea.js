import BackgroundShapes from './BackgroundShapes';
import UserProfile from './UserProfile';
import NotesSection from './NotesSection';
import VersesSection from './VersesSection';
import SearchBar from './SearchBar';
import ThemeSelector from './ThemeSelector';


function ContentArea() {
  // Dados fictícios para teste
  const annotations = [
    {
      title: "Anotação 1",
      content: "Este é o conteúdo da anotação 1. Aqui pode ir uma explicação mais detalhada ou um comentário.",
      start_verse: "Gênesis 1:1",
      end_verse: "Gênesis 1:2"
    },
    {
      title: "Anotação 2",
      content: "Este é o conteúdo da anotação 2. Pode ser uma reflexão pessoal, um insight ou uma dúvida.",
      start_verse: "Mateus 5:3",
      end_verse: "Mateus 5:10"
    }
  ];


  const userData = {
    name: "Vitor Rios Rodrigues",
    image: "https://randomuser.me/api/portraits/men/1.jpg"
  };


  const verses = [
    {
      number: 1,
      text: "No princípio, Deus criou os céus e a terra.",
      book: "Gênesis",
      chapter: 1
    },
    {
      number: 2,
      text: "A terra era sem forma e vazia; e havia trevas sobre a face do abismo, e o Espírito de Deus se movia sobre a face das águas.",
      book: "Gênesis",
      chapter: 1
    },
    // Adicione mais versículos conforme necessário
  ];
  

    return (
      <div className="container mx-auto h-screen py-16 px-8 relative">
        <UserProfile user={userData} />
        <NotesSection annotations={annotations}/>
        <VersesSection verses={verses} />
        <ThemeSelector />
      </div>
    );
  }
  export default ContentArea;
