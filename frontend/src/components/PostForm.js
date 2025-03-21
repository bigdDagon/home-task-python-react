import React, { useState } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";
import {
  Container,
  Typography,
  Button,
  TextField,
  Box
} from "@mui/material";

const PostForm = () => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const navigate = useNavigate();
  const { id } = useParams();

  React.useEffect(() => {
    if (id) {
      const fetchPost = async () => {
        const response = await axios.get(
          `http://localhost:5000/api/posts/${id}`
        );
        setTitle(response.data.title);
        setContent(response.data.content);
      };
      fetchPost();
      
    }
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const postData = { title, content };

    try {
      if (id) {
        await axios.put(`http://localhost:5000/api/posts/${id}`, postData);
      } else {
        await axios.post("http://localhost:5000/api/posts", postData);
      }
      navigate("/");
    } catch (error) {
      console.error("Error saving post:", error);
    }
  };

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" gutterBottom>
        {id ? "Edit Post" : "Create Post"}
      </Typography>
      <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
        <TextField
          fullWidth
          label="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          variant="outlined"
          margin="normal"
          inputProps={{ maxLength: 100 }}
        />
        <TextField
          fullWidth
          label="Content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          required
          variant="outlined"
          margin="normal"
          multiline
          rows={4}
        />
        <Button type="submit" variant="contained" color="primary" sx={{ mt: 2 }}>
          Save
        </Button>
      </Box>
    </Container>
  );
};

export default PostForm;
