import React from "react";
import { useAuth0 } from "@auth0/auth0-react";

const Logout = () => {
  const { logout } = useAuth0();

  return (
    <li onClick={() => logout({ returnTo: window.location.origin })}>
      <a>Log Out</a>
    </li>
  );
};

export default Logout;