// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "../node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract diplomaNFT is ERC721 {
    uint256 public tokenId;
    address public owner;

    struct DiplomaData {
        string pdfUrl;
        string jsonUrl;
        bytes32 pdfHash;
    }

    mapping(uint256 => DiplomaData) private _tokenData;

    constructor() ERC721("diplomaNFT", "DNFT") {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    function mintDiploma(
        address recipient,
        string memory pdfUrl,
        string memory jsonUrl,
        bytes32 pdfHash
    ) public onlyOwner returns (uint256) {
        _safeMint(recipient, tokenId);

        DiplomaData memory data = DiplomaData(pdfUrl, jsonUrl, pdfHash);
        _tokenData[tokenId] = data;

        tokenId++;
        return tokenId;
    }

    function getTokenData(
        uint256 tokenId
    )
        public
        view
        returns (string memory pdfUrl, string memory jsonUrl, bytes32 pdfHash)
    {
        require(_exists(tokenId), "ERC721: URI query for nonexistent token");

        pdfUrl = _tokenData[tokenId].pdfUrl;
        jsonUrl = _tokenData[tokenId].jsonUrl;
        pdfHash = _tokenData[tokenId].pdfHash;
    }

    function burnDiploma(uint256 tokenId) public onlyOwner {
        _burn(tokenId);
        delete _tokenData[tokenId];
    }
}
